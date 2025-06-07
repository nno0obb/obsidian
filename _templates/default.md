---

# # TSIA

...

---

> [!info] Keywords
> - ...

> [!tip] Refs
> - ...

<%*
tR += "> [!multi-column]\n"
tR += ">\n"
tR += ">> [!cite] Tags\n"
tR += ">> - ...\n"
tR += ">> - ...\n"
tR += ">\n"
tR += ">> [!example] Paths\n"
let paths = tp.file.path(true).split("/");
paths.pop()
paths.forEach((path, idx) => {
	let indent = " ".repeat(idx * 2)
	tR += `>> ${indent} - [[🔖 ${path}]]\n`
})
%>