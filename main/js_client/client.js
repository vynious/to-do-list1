const contentContainer = document.getElementById('content-container')
const createForm = document.getElementById('note-form')
const baseEndpoint = 'http://localhost:8000/tdl'

if (createForm) {
    createForm.addEventListener('submit',handleCreate)
}


function handleCreate(event) {
    event.preventDefault()
    const createEndpoint = `${baseEndpoint}/create/`
    let createNoteData = new FormData(createForm)
    let createNoteObjectData = Object.fromEntries(createNoteData)
    let bodyStr = JSON.stringify(createNoteObjectData)
    console.log('eee')
    console.log(bodyStr)
    const options ={
        method:'POST',
        headers:{
            'Content-Type':'application/json',

        },
        body:bodyStr,
    }
    fetch(createEndpoint,options)
    .then(response=>{
        console.log(response.json())
    })

}


// function getNoteList() {
//     const listEndpoint = `${baseEndpoint}/`
//     const options = {
//         method:'GET',
//         headers:{
//             'Content-Type':'application/json',    
//         }
//     }
//     fetch(listEndpoint,options)
//     .then(response=>{
//         return response.json()
//     })
//     .then(data=>{
//         console.log(data)
//         writeToContainer(data)
//     })
//     .catch(err=>{
//         console.log(`${err.message}`)
//     })
// }

async function getNoteList(){
    const listEndpoint = `${baseEndpoint}/`
    const response = await fetch(listEndpoint,{
        method:'GET',
        headers:{
            'Content-Type':'application/json',
 
        }
    })
    const data = await response.json()
    writeToContainer(data)
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML='<pre>'+JSON.stringify(data.results,null,4)+'</pre>'
    }

}

getNoteList()