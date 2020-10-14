document.addEventListener("DOMContentLoaded", ()=> {

    const url = "http://127.0.0.1:8000/api/artist_list/"
    let artistList = document.getElementById("artists")

        fetch(url).then(data=>data.json()).then(obj=>{
        for (let artist of obj) {
            let h2 = document.createElement('h2')

            if (artist.surname == null){
                h2.innerText = artist.name
            } else {
                h2.innerText = `${artist.name} ${artist.surname}`
            }

            artistList.appendChild(h2)

        }

    })
    .catch(error => {
        console.log(error)
    })

})