document.addEventListener('DOMContentLoaded', (event) => {
    const selects = document.querySelectorAll('select[name="producto"]');

    selects.forEach((select, index) => {
        select.addEventListener('change', () => {
            selects.forEach((s, i) => {
                if (i !== index) {
                    s.selectedIndex = 0;
                }
            });
        });
    });
});