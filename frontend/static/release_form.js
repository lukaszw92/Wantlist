document.addEventListener("DOMContentLoaded", ()=> {

    const artists_url = "http://127.0.0.1:8000/api/artist_list/"
    const genres_url = "http://127.0.0.1:8000/api/genre_list/"

    let artistList = document.getElementById("artist")
    let genreList = document.getElementById("genre")

        fetch(artists_url).then(data=>data.json()).then(obj=>{
        for (let artist of obj) {
            let option = document.createElement('option')

            if (artist.surname == null){
                option.innerText = artist.name
            } else {
                option.innerText = `${artist.name} ${artist.surname}`
            }

            option.value = artist.id

            artistList.appendChild(option)

        }

    })

          fetch(genres_url).then(data=>data.json()).then(obj=>{
        for (let genre of obj) {
            let option = document.createElement('option')

            option.innerHTML = genre.name
            option.value = genre.id
            genreList.appendChild(option)

        }

    })

    .catch(error => {
        console.log(error)
    })




})