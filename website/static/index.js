// Function for deleteing a note. Its called from the home.html file.

function deleteNote(noteId) {
    // passes in the note id from the item the button was clicked on
    fetch('/delete-note', {
        method: 'POST',
        body: JSON.stringify({noteId: noteId})
    }).then((_res) => {
        // refreshes the page so the note disappears when the button is clicked on
        window.location.href = '/';
    });
}