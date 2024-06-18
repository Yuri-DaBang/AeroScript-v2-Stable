
Posts = ["Hello i am hamza","No i am hamza","But i am also hamza","you all are liers , only i am hamza"]

fun RedirectHome(writer, request) {
   writer.write(``<html lang="en" class="dark-mode"><head>
            <title>F COMMUNITY</title></head><body>``)
   for n in 0..len(Posts) {

         fhtml0 = ``<span style="color:#24292e;font-family:consolas;font-size:15px;padding:5px;margin:6px;">``
         fhtml1 = n
         fhtml1_2 = Posts[n]
         fhtml2 = ``</span><hr>``
         fhtmlc = fhtml0 + fhtml1+ fhtml1_2 +fhtml2
         writer.write(fhtmlc)

   }
   writer.write(``</body>``)

}

# In browser, navigate to http://localhost:9090/ page

http.handleFunc("/", RedirectHome)
http.handleFunc("/home", RedirectHome)

fmt.Println("* Starting on `127.0.0.1:9090`")

let ret = http.listenAndServe("127.0.0.1:9090")
if (ret == false) {
	println("listenAndServe failed, error:", ret.message())
}

