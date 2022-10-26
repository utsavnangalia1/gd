// const searchForm = document.getElementById('search-form_qna')
// const searchInput = document.getElementById('search-input_qna')
// const searchdisp = document.getElementById('search-display_qna')

// const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

// const sendSearchData = (word) =>{
//     $.ajax({
//         type: "POST",
//         url: 'search/',
//         data: {
//             'csrfmiddlewaretoken': csrf,
//             'shabd': word,
//         },
//         success: (res) => {
//             console.log(res)
//             const shabd = res.data
//             console.log(shabd)
//             if (Array.isArray(shabd)){
//                 console.log("kya")
//                 searchdisp.innerHTML = ``
//                 shabd.forEach(word => {
//                     searchdisp.innerHTML += `
//                     <div class="wordunit">
//                         <div class="one">
//                             <p style="background-color:#e3e379;">${word.meaning}</p>
//                             <p>${word.eng}</p>
//                             <p>${word.sanskt}</p>
//                            <p style="margin-bottom:0px;">${word.gramgp}</p>
//                         </div> 
//                     </div>`
//                 })
//             }
//             else{
//                 if(searchInput.value.length > 0)
//                 {
//                     searchdisp.innerHTML = `<br \><h3 style="text-align:center;">${shabd}</h3>`
//                     console.log("kyabe")
//                 }
//                 else{
//                     searchdisp.classList.add('not-visible')
//                 }
//             }
//         },
//         error: (err) => {
//             console.log(err)
//         }
//     })        
// }

// searchInput.addEventListener('keyup', e=>{
//     console.log(e.target.value)

//     if (searchdisp.classList.contains('not-visible')){
//         searchdisp.classList.remove('not-visible')
//     }

//     sendSearchData(e.target.value)
// })

// searchInput.addEventListener('keyup', e => {
//     console.log(e.target.value)


//     sendSearchData(e.target.value)
// })

const popup1 = document.getElementById('add-question')
var openPopup1 = document.getElementById('add')
var closePopup1 = document.getElementById('close')

openPopup1.addEventListener('click', () => {
	popup1.style.display = "block";

})

closePopup1.addEventListener('click', () => {
	popup1.style.display = "none";
})

