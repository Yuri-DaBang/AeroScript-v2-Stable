//////////////////////////////////
//////                      //////
////// THE GRAND SPEED TEST ////// 
//////                      //////
//////////////////////////////////

////// TEST 1 //////

//fmt.Println(time.Now)

fun test1(Mrange) {
    st = time.Now("")
    println("ST: ",st)
    tlist = []    

    for i in 1..Mrange {
        tlist += (i)
        //print(i)
        //os.system('cls')
    }
    //println(tlist)
    et = time.Now()
    println("ET: ",et)
    fmt.Println('[*1] Process Done!: {Mrange}')
    return 'int({et}) - int({st})'
}  

fun test2(Mrange) {
    st = time.Now()
    println("ST: ",st)

    tlist = 0   

    for i in 1..Mrange {
        tlist += 1
        //print(i)
        //os.system('cls')
    }
    et = time.Now()
    println("ET: ",et)
    println('[*2] Process Done!: {Mrange}')
    return 'int({et}) - int({st})'
}

test1(1000000)