function updatePlayer(trackId) {
    let url = 'https://open.spotify.com/embed/track/' + trackId;
    document.getElementById('player').setAttribute('src', url);
    console.log('player updated - url: ', url);
};

document.querySelectorAll('.bracket-round div').forEach(item => {
    item.addEventListener('click', function(event) {
        console.log('.bracket-round div clicked');
        let trackId = item.dataset.trackId;
        updatePlayer(trackId);
    });
});

document.querySelectorAll('li').forEach(item => {
    item.addEventListener('click', function(event) {
        console.log('li clicked');
        let trackId = item.querySelector('.group-entry').dataset.trackId;
        updatePlayer(trackId);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const allTracks = document.querySelectorAll('.entry');
    const idx = Math.floor(Math.random() * allTracks.length);
    let trackId = allTracks[idx].dataset.trackId;
    updatePlayer(trackId);
});
