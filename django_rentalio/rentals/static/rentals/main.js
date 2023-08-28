const form = document.getElementById("search-form")
const input = document.getElementById("id_search")


const BOOK_ID_LENGTH = 24

input.focus()

input.addEventListener("keyup",()=> {
    if (input.value.length === 24) {
        form.submit()
    }

})