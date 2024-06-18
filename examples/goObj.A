fmt.Printf("Hello %s!\n", "go function");
fmt.Printf("%v\n", os.Args)

let f, err = os.Open("./mdoc.go")
if (err != nil) { // or 'if err {' 
    fmt.Println(f, err)
} else {
    fmt.Println(f, err)
}

let name,_ = os.Hostname
fmt.Println("HOSTNAME: ",name)

i = rand.Int
fmt.Println("RANDOM NUM: ",i)

let files, err = ioutil.ReadDir(".")
if err != nil {
	log.Fatal(err)
}

for file in files {
	if file.Name() == ".git" {
		continue
	}
	fmt.Printf("Name=%s, Size=%d\n", file.Name(), file.Size())
}

for s in regex.MustCompile(``[\s_]``).Split("foo_bar_baz", -1) {
  println(s)
}

println(runtime.OS)
println(runtime.ARCH)