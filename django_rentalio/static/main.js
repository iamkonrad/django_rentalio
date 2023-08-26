console.log('hello world from base dir')

const head = document.getElementById('head')

if (head) {
    const goBackBtn = document.getElementById('go-back-btn')
    gobackBtn?.addEventListener('click',()=> history.back())
}