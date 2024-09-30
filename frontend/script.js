const tbody = document.querySelector('#body') 
const btn = document.querySelector('.add-btn')
const modal = document.querySelector('.modal')
const close = document.querySelector('.close')
const form = document.querySelector('form')

const descripcion = document.querySelector('#descripcion')
const date = document.querySelector('#date')
const category = document.querySelector('#category')

const API = 'http://127.0.0.1:8000/'



let mode = 'add'
let editId = ''

const modalToggle = () => modal.classList.toggle('show')

btn.addEventListener('click',modalToggle)
close.addEventListener('click', () => {
     form.reset()
    modalToggle()
})



function formatDate(date) { 
    return new Date(date).toLocaleDateString('es-ES',{
        month:'long',
        day:'2-digit',
        year:'numeric'
    }) 
}



async function getlist() {
    try {
        const data = await fetch(API)
        const rest = await data.json()
    
        rest.tasks.forEach( (task,i) => {    
            const tr = document.createElement('tr')
            

            tr.innerHTML = `
            <td>${task.description}</td>
            <td class="completed ${task.completed ? 'true' : ''}">${task.completed ?  'Completado' : 'Incompleto'}</td>
            <td>${formatDate(task.due_date) }</td>
            <td>${task.category}</td>
            <td>${task.reminder ? 'Recordar' : 'No recordar' }</td>
            <td class="actions">
                  <button onclick="removeTaskById(${i + 1})">Eliminar</button>
                  <button onclick="editTask(${i})">Editar</button>
            </td>
            `
            
            tbody.appendChild(tr)
        });

    } catch (error) {
        console.log(error);
            
    }


}

getlist()

async function editTask(id) { 
    mode = 'edit'
    editId = id
    modalToggle()
    const data = await getTaskById(id)
    const task = data.task

    form.description.value = task.description
    form.due_date.value = task.due_date
    form.category.value = task.category.toLocaleLowerCase()
    
 }


async function removeTaskById(id) { 
    const response = await fetch(API + id,{
        method:'DELETE',
    
    })
    const datos = await response.json()

    console.log(datos);
    
 }
async function editTaskById(id,task) { 
    // editar tarea

    const response = await fetch(`${API}${id + 1}`,{
        body:JSON.stringify({...task, completed:false,reminder:false}),
        method:'PUT',
        headers:{
            'Content-Type':'application/json'
        }
    
    })
    const datos = await response.json()

    console.log(datos);
    
}


async function getTaskById(id){
    const response = await fetch(API+id)
    const task = await response.json()
    return task
}



form.addEventListener('submit',async (e) => {
    e.preventDefault()
    const formd = new FormData(e.target)
    const data = Object.fromEntries(formd)

    if (mode === 'add') {
        console.log(data);
        
    
        const response = await fetch(API,{
            body:JSON.stringify({... data, completed:false,reminder:false}),
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            }
        })
    
        const datos = await response.json()
    
        console.log(datos);
    }else{
       await editTaskById(editId,data)
    }
    
    
})
