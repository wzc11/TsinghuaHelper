function validat() {
	var i = document,
		c = "getElementById",
		h = i[c]("form"),
		e = i[c]("zh"),
		b = i[c]("mm"),
		a = i[c]("czm");
	if (e.value == "") {
		e.focus();
		alert("请输入账号！");
		return false;
	}
	if (b.value == "") {
		b.focus();
		alert("请输入密码！");
		return false;
	}

}
