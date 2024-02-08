function meanCheck(num) {
    me = document.querySelectorAll(".meanAnswer")[num]
    me.style = "color: black"

    inputbox = document.querySelectorAll(".meanA")[num]
    inputbox.disabled = "true"
} 

function wordCheck(num) {
    me = document.querySelectorAll(".wordAnswer")[num]
    me.style = "color: black"

    inputbox = document.querySelectorAll(".wordA")[num]
    inputbox.disabled = "true"
}