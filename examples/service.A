//service Hello on "127.0.0.1:8090" {
service Hello on "127.0.0.1:8090:debug" { //':debug': for debugging request
  @route(url="/authentication/login/{username}/{password}", methods=["POST"])
  fun login(writer, request) {
    //writer.writeJson({ sessionId: "3d5bd2cA15ef047689" })
    //writer.writeJson({ sessionId: "3d5bd2cA15ef047689" }), 200 # same as above
    //return { sessionId: "3d5bd2cA15ef047689" }, 200 # same as above

    USERNAME , PASSWORD = vars["username"] , vars["password"]
    RESPONCE = ""

    if USERNAME {
        if USERNAME == "hamza" {
            RESPONCE += "User Identified!..."
            if PASSWORD == "hamza" {
                RESPONCE += "Password >> OKAY..."
            } else {
                RESPONCE += "Wronf Password!..."
            }
        } else {
            RESPONCE += "User not Identified!..."
        }
    } else {
        RESPONCE += "PLEASE PROVIDE A USERNAME!!!!"
    }

    return { sessionId: "3d5bd2cA15ef047689", _responce:RESPONCE } //same as above
  }

  @route(url="/authentication/logout", methods=["POST"])
  fun logout(writer, request) {
    // writer.writeHeader(http.STATUS_CREATED) # return http status code 201
    return http.STATUS_CREATED //same as above
  }

  @route(url="/meters/setting-result/{acceptNo}", methods=["GET"])
  fun load_survey_result(writer, request) {
    //using 'vars' dictionary to access the url parameters
    //writer.writeJson({ acceptNo: vars["acceptNo"], resultCode: "1"})
    return { acceptNo: vars["acceptNo"], resultCode: "1"} //same as above
  }

  @route(url="/articles/{category}/{id:[0-9]+}", methods=["GET"])
  fun getArticle(writer, request) {
    //using 'vars' dictionary to access the url parameters
    //writer.writeJson({ category: vars["category"], id: vars["id"]})
    return { category: vars["category"], id: vars["id"]} //same as above
  }
}
