document.addEventListener('DOMContentLoaded', (event) => {
    function updatedate() {
        let now = new Date();

        let year = now.getFullYear();
        let month = (now.getMonth() + 1).toString().padStart(2, '0');
        let day = now.getDate().toString().padStart(2, '0');

        document.getElementById('current-time').innerHTML = `${year}-${month}-${day}`;
    }

    updatedate();
});
