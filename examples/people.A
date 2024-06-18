class Person {
	let firstName;
	let lastName;
	let nickName;

	fn init(firstname, lastname="sufyan", nickname="hamza zabar a , hamza zer e , hamza paish o, a , e , o") {
		this.firstName = firstname
		this.lastName = lastname
		this.nickName = nickname
	}

	private fn Msg(extra1, extra2="extra2", args...) {
		printf("firstName=%s, lastName=%s, nickName=%s\n", firstName, lastName, nickName)
		printf("extra1=%s, extra2=%s\n", extra1, extra2)
		for i in args {
			printf("i := %v\n", i)
		}
	}
}

obj = new Person("hamza")
obj.Msg("extra1", "Hello", 1, [1,2,3], (4,5,6))

println()
obj.Msg("extra1")