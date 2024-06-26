# AeroScript Programming Language
## Summary

🌟 **AeroScript**: A Versatile Custom Language Interpreter
- NOTE: `AeroScript` will be mentained on `Fri3nds Group Org `at [Fri3nds Group](https://github.com/Fri3ndsGroup) 

🛠️ **AeroScript** is a custom language interpreter crafted in Go. Boasting C-style syntax, it draws significant inspiration from Ruby, Python, Perl, and C#.

✨ **Features**:
- Supports normal control flow, functional programming, and object-oriented programming.
- Allows importing Go modules seamlessly.
- Includes a simple debugger for an enhanced coding experience.

💻 I also created a simple programming language using **AeroScript** itself!

## New Update

* Added `console`, `log`, `os`, `runtime`, `time`, `bufio`, `regex`, `strings`, `bytes`, `cryptomd5`, `cryptosha1`, `cryptosha256`, `cryptosha512`, `base64`, `json`, `xml`, `errors`, `io`, `ioutil`, `math`, `rand`, `net`, `nethttp`, `neturl`, `filepath`

Tree of subcommands:

console:
  - Errorf
  - Println
  - Print
  - Printf
  - Fprint
  - Fprintln
  - Fscan
  - Fscanf
  - Fscanln
  - Scan
  - Scanf
  - Scanln
  - Sscan
  - Sscanf
  - Sscanln
  - Sprint
  - Sprintf
  - Sprintln

log:
  - Fatal
  - Fatalf
  - Fatalln
  - Flags
  - Panic
  - Panicf
  - Panicln
  - Print
  - Printf
  - Println
  - SetFlags
  - SetOutput
  - SetPrefix

os:
  - Chdir
  - Chmod
  - Chown
  - Exit
  - Getpid
  - Hostname
  - Environ
  - Getenv
  - Setenv
  - Create
  - Open

runtime:
  - OS
  - ARCH

time:
  - After
  - Sleep
  - Tick
  - Since
  - FixedZone
  - LoadLocation
  - NewTicker
  - Date
  - Now
  - Parse
  - ParseDuration
  - ParseInLocation
  - Unix
  - AfterFunc
  - NewTimer
  - Nanosecond
  - Microsecond
  - Millisecond
  - Second
  - Minute
  - Hour

bufio:
  - NewWriter
  - NewReader
  - NewReadWriter
  - NewScanner

regex:
  - Match
  - MatchReader
  - MatchString
  - QuoteMeta
  - Compile
  - CompilePOSIX
  - MustCompile
  - MustCompilePOSIX

strings:
  - Compare
  - Contains
  - ContainsAny
  - ContainsRune
  - Count
  - EqualFold
  - Fields
  - FieldsFunc
  - HasPrefix
  - HasSuffix
  - Index
  - IndexAny
  - IndexByte
  - IndexFunc
  - IndexRune
  - Join
  - LastIndex
  - LastIndexAny
  - LastIndexByte
  - LastIndexFunc
  - Map
  - Repeat
  - Replace
  - ReplaceAll
  - Split
  - SplitAfter
  - SplitAfterN
  - SplitN
  - Title
  - ToLower
  - ToLowerSpecial
  - ToTitle
  - ToTitleSpecial
  - ToUpper
  - ToUpperSpecial
  - Trim
  - TrimFunc
  - TrimLeft
  - TrimLeftFunc
  - TrimPrefix
  - TrimRight
  - TrimRightFunc
  - TrimSpace
  - TrimSuffix

bytes:
  - Compare
  - Contains
  - ContainsAny
  - ContainsRune
  - Count
  - Equal
  - EqualFold
  - Fields
  - FieldsFunc
  - HasPrefix
  - HasSuffix
  - Index
  - IndexAny
  - IndexByte
  - IndexFunc
  - IndexRune
  - Join
  - LastIndex
  - LastIndexAny
  - LastIndexByte
  - LastIndexFunc
  - Repeat
  - Replace
  - Split
  - SplitAfter
  - SplitAfterN
  - SplitN
  - Title
  - ToLower
  - ToTitle
  - ToUpper
  - Trim
  - TrimFunc
  - TrimLeft
  - TrimLeftFunc
  - TrimPrefix
  - TrimRight
  - TrimRightFunc
  - TrimSpace
  - TrimSuffix

cryptomd5:
  - New
  - Sum

cryptosha1:
  - New
  - Sum

cryptosha256:
  - New
  - Sum

cryptosha512:
  - New
  - Sum

base64:
  - NewDecoder
  - NewEncoder
  - StdEncoding
  - URLEncoding

json:
  - Marshal
  - Unmarshal
  - NewDecoder
  - NewEncoder
  - MarshalIndent

xml:
  - Marshal
  - Unmarshal
  - NewDecoder
  - NewEncoder
  - MarshalIndent

errors:
  - New
  - Is
  - As

io:
  - Copy
  - CopyBuffer
  - CopyN
  - ReadAtLeast
  - ReadFull
  - WriteString

ioutil:
  - ReadAll
  - ReadFile
  - ReadDir
  - WriteFile
  - TempDir
  - TempFile

math:
  - Abs
  - Acos
  - Asin
  - Atan
  - Atan2
  - Ceil
  - Cos
  - Cosh
  - Exp
  - Exp2
  - Expm1
  - Floor
  - Log
  - Log10
  - Log1p
  - Log2
  - Max
  - Min
  - Pow
  - Sin
  - Sinh
  - Sqrt
  - Tan
  - Tanh

rand:
  - New
  - NewSource
  - ExpFloat64
  - Float32
  - Float64
  - Int
  - Int31
  - Int31n
  - Int63
  - Int63n
  - Intn
  - NormFloat64
  - Perm
  - Seed
  - Uint32
  - Uint64

net:
  - CIDRMask
  - Dial
  - DialTimeout
  - FileConn
  - FileListener
  - FilePacketConn
  - IPv4
  - IPv4Mask
  - Listen
  - LookupAddr
  - LookupCNAME
  - LookupHost
  - ParseCIDR
  - ParseIP
  - SplitHostPort
  - JoinHostPort

nethttp:
  - Get
  - Post
  - PostForm
  - Head
  - ListenAndServe
  - NewRequest
  - ReadResponse
  - Redirect
  - Serve
  - ServeContent
  - ServeFile
  - SetCookie

neturl:
  - Parse
  - ParseRequestURI
  - QueryEscape
  - QueryUnescape

filepath:
  - Abs
  - Base
  - Clean
  - Dir
  - Ext
  - FromSlash
  - Glob
  - IsAbs
  - Join
  - Match
  - Rel
  - Split
  - ToSlash
  - VolumeName
  - Walk

## Credits

- **mayoms**:
  - This project is based on mayoms's [monkey](https://github.com/mayoms/monkey) interpreter.

## License

This project is licensed under the MIT License.

