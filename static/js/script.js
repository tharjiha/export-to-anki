//PASTING BUTTON SCRIPT
const textarea = document.getElementById('user_text');
const pasteBtn = document.getElementById('pasteBtn');

pasteBtn.addEventListener('click', async () => {
    try{
        const text = await navigator.clipboard.readText(); //get text from keyboard

        //put cursor at right place
        const start = textarea.selectionStart;
        const end = textarea.selectionEnd;
        const before = textarea.value.substring(0, start);
        const after = textarea.value.substring(end);
        textarea.value = before + text + after;

        textarea.selectionStart = textarea.selectionEnd = start + text.length;
        textarea.focus();
    }

    catch (err) {
        alert('Failed to read clipboard contents: ' + err);
    }
});

