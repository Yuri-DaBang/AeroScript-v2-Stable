let handler = fun(writer, request) {
	writer.write("<h1>HELLO HTTP CLIENT , I AM SERVER!</h1>")
}

http.listenAndServe("127.0.0.1:8080", handler)
//Same as above
//http.listenAndServe("127.0.0.1:8080", fn(writer, request) {
//	writer.write("Hello HTTP client, I'm server")
//})