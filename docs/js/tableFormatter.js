function clickSkillTag(e, formID){
  e.target.classList.toggle("selected")
  formatTable(formID)
}

function formatTable(formID){
  const form = document.getElementById(formID)
  // For convenience, we assume there is only one table
  // which makes it easier to interop with markdown
  const table = document.getElementsByTagName("table")[0]

  const selectedSkills = new Set()
  const selectedButtons = form.getElementsByClassName("selected")
  for(let b of selectedButtons){
    selectedSkills.add(b.innerText)
  }
  
  const availableSkills = new Set()
  for(let i = 1; i < table.rows.length; i++){
    const row = table.rows[i];
    const rowSkills = new Set(row.cells[2].innerText.split(",").map((s) => s.trim()))
    const rowSkillsSelected = rowSkills.intersection(selectedSkills)
    console.log(rowSkillsSelected)
    if(rowSkillsSelected.size === selectedSkills.size){
      row.removeAttribute("hidden")
      rowSkills.forEach((s) => availableSkills.add(s))
    } else {
      row.setAttribute("hidden", "")
    }
  }

  const allButtons = form.getElementsByClassName("skill")
  for(let b of allButtons){
    console.log(b.innerText)
    if(availableSkills.has(b.innerText)){
      b.removeAttribute("disabled")
    } else {
      b.setAttribute("disabled", "")
    }
  }
}