package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"mime/multipart"
	"net/http"
	"os"
	"path/filepath"
)

const (
	API_URL             = "http://127.0.0.1:5000/"
	LIBS_DIR            = "./cli/aeromod"
	FRAMEWORKS_DIR      = "./cli/frameworks"
	CONF_FILE           = "./server/items/libs/conf.json"
	FRAMEWORK_CONF_FILE = "./server/items/framework/conf.json"
	CHUNK_SIZE          = 1024 * 1024 // 1 MB chunk size for reading/writing
)

// Config represents the structure of conf.json
type Config struct {
	Files map[string]string `json:"files"`
}

var (
	DefaultPassword = "" // Default password for files pushed without specific password
)

// pushFile sends a file to the server with authentication
func pushFile(filePath string, password string) error {
	file, err := os.Open(filePath)
	if err != nil {
		return fmt.Errorf("could not open file: %v", err)
	}
	defer file.Close()

	fileInfo, err := file.Stat()
	if err != nil {
		return fmt.Errorf("could not get file info: %v", err)
	}
	fileSize := fileInfo.Size()

	body := &bytes.Buffer{}
	writer := multipart.NewWriter(body)
	part, err := writer.CreateFormFile("file", filepath.Base(file.Name()))
	if err != nil {
		return fmt.Errorf("could not create form file: %v", err)
	}

	progress := NewProgressBar(fileSize)
	reader := io.LimitReader(file, fileSize)
	chunk := make([]byte, CHUNK_SIZE)

	for {
		n, err := reader.Read(chunk)
		if err != nil && err != io.EOF {
			return fmt.Errorf("error reading file: %v", err)
		}
		if n == 0 {
			break
		}

		_, err = part.Write(chunk[:n])
		if err != nil {
			return fmt.Errorf("error writing to form part: %v", err)
		}

		progress.Update(int64(n))
	}

	writer.Close()

	request, err := http.NewRequest("POST", API_URL+"update", body)
	if err != nil {
		return fmt.Errorf("could not create request: %v", err)
	}
	request.Header.Set("Content-Type", writer.FormDataContentType())

	config, err := readConfig(CONF_FILE)
	if err != nil {
		return fmt.Errorf("could not read config: %v", err)
	}

	if password != "" {
		config.Files[filepath.Base(filePath)] = password
	} else {
		config.Files[filepath.Base(filePath)] = DefaultPassword
	}

	err = writeConfig(CONF_FILE, config)
	if err != nil {
		return fmt.Errorf("could not write config: %v", err)
	}

	request.SetBasicAuth("", config.Files[filepath.Base(filePath)])

	response, err := http.DefaultClient.Do(request)
	if err != nil {
		return fmt.Errorf("could not make request: %v", err)
	}
	defer response.Body.Close()

	if response.StatusCode != http.StatusOK {
		return fmt.Errorf("failed to upload file: %s", response.Status)
	}

	fmt.Println("\nFile uploaded successfully")
	return nil
}

// pushFramework sends a framework directory to the server with authentication
func pushFramework(dirPath string, password string) error {
	// Code to push a directory similar to pushFile
	return nil
}

// pullFile downloads a file from the server with authorization
func pullFile(packageName string, authToken string) error {
	request, err := http.NewRequest("GET", API_URL+"get/"+packageName, nil)
	if err != nil {
		return fmt.Errorf("could not create request: %v", err)
	}

	config, err := readConfig(CONF_FILE)
	if err != nil {
		return fmt.Errorf("could not read config: %v", err)
	}

	password, ok := config.Files[packageName]
	if !ok {
		return fmt.Errorf("password not found for %s", packageName)
	}

	if authToken != "" && authToken != password {
		return fmt.Errorf("invalid auth token")
	}

	request.SetBasicAuth("", password)

	response, err := http.DefaultClient.Do(request)
	if err != nil {
		return fmt.Errorf("error downloading %s: %v", packageName, err)
	}
	defer response.Body.Close()

	if response.StatusCode != http.StatusOK {
		return fmt.Errorf("error downloading %s: %s", packageName, response.Status)
	}

	contentLength := response.ContentLength
	os.MkdirAll(LIBS_DIR, os.ModePerm)
	filePath := filepath.Join(LIBS_DIR, packageName)
	outFile, err := os.Create(filePath)
	if err != nil {
		return fmt.Errorf("error creating file %s: %v", filePath, err)
	}
	defer outFile.Close()

	progress := NewProgressBar(contentLength)

	_, err = io.Copy(outFile, io.TeeReader(response.Body, &progressWriter{Writer: outFile, Progress: &progress, Total: contentLength}))
	if err != nil {
		return fmt.Errorf("error saving file %s: %v", filePath, err)
	}

	fmt.Printf("\nDownloaded %s to %s\n", packageName, LIBS_DIR)
	return nil
}

// pullFramework downloads a framework directory from the server with authorization
func pullFramework(dirName string, authToken string) error {
	// Code to pull a directory similar to pullFile
	return nil
}

// readConfig reads the configuration from conf.json
func readConfig(filePath string) (*Config, error) {
	config := &Config{
		Files: make(map[string]string),
	}

	if _, err := os.Stat(filePath); !os.IsNotExist(err) {
		data, err := ioutil.ReadFile(filePath)
		if err != nil {
			return nil, err
		}
		err = json.Unmarshal(data, config)
		if err != nil {
			return nil, err
		}
	}

	return config, nil
}

// writeConfig writes the configuration to conf.json
func writeConfig(filePath string, config *Config) error {
	data, err := json.MarshalIndent(config, "", "  ")
	if err != nil {
		return err
	}
	err = ioutil.WriteFile(filePath, data, 0644)
	if err != nil {
		return err
	}
	return nil
}

// NewProgressBar creates a new progress bar with total size
func NewProgressBar(total int64) ProgressBar {
	return ProgressBar{Total: total}
}

// ProgressBar represents a simple text-based progress bar
type ProgressBar struct {
	Total int64
}

// Update updates the progress bar with current progress
func (p *ProgressBar) Update(current int64) {
	progress := float64(current) / float64(p.Total) * 100
	fmt.Printf("\rProgress: %.2f%%", progress)
}

// progressWriter wraps around a writer to update progress
type progressWriter struct {
	io.Writer
	Progress *ProgressBar
	Total    int64
}

// Write writes data to the underlying writer and updates progress
func (pw *progressWriter) Write(p []byte) (int, error) {
	n, err := pw.Writer.Write(p)
	if err == nil {
		pw.Progress.Update(int64(n))
	}
	return n, err
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Usage: go run mod.go <push|pull|pushFramework|pullFramework> <file_path> [-password <password> | -auth <auth_token>]")
	}

	command := os.Args[1]
	filePath := os.Args[2]

	switch command {
	case "push":
		password := DefaultPassword
		if len(os.Args) > 4 && os.Args[3] == "-password" {
			password = os.Args[4]
		}
		if err := pushFile(filePath, password); err != nil {
			fmt.Println(err)
		}
	case "pull":
		authToken := DefaultPassword
		if len(os.Args) > 4 && os.Args[3] == "-auth" {
			authToken = os.Args[4]
		}
		if err := pullFile(filepath.Base(filePath), authToken); err != nil {
			fmt.Println(err)
		}
	case "push-framework":
		password := DefaultPassword
		if len(os.Args) > 4 && os.Args[3] == "-password" {
			password = os.Args[4]
		}
		if err := pushFramework(filePath, password); err != nil {
			fmt.Println(err)
		}
	case "pull-framework":
		authToken := DefaultPassword
		if len(os.Args) > 4 && os.Args[3] == "-auth" {
			authToken = os.Args[4]
		}
		if err := pullFramework(filepath.Base(filePath), authToken); err != nil {
			fmt.Println(err)
		}
	default:
		fmt.Println("Unknown command. Use 'push', 'pull', 'pushFramework', or 'pullFramework'.")
	}
}
