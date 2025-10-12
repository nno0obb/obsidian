---
created_at: 2025/06/14 22:48:34
updated_at: 2025/06/14 22:49:49
---
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