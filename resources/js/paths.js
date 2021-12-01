'use strict';

let globals = {}

const renderPathsAsMap = (solutions) => {
    const parentDiv = document.getElementById('paths')
    let counter = 0
    const solutionsDiv = document.getElementById('solutions')
    if (solutionsDiv) {
        parentDiv.innerHTML = ""

    }
    for (const pathArray of solutions) {
        const newNode = document.createElement('div')
        newNode.setAttribute('id', 'solutions')
        let text = "" + counter + ". "
        for (const path of pathArray) {
            text = text + path + " => "
        }
        text = text.substring(0, text.length - 4);
        text = text + '; distance = ' + (parseInt(pathArray.length) - 1)
        newNode.innerHTML = text
        parentDiv.appendChild(newNode)
        counter = counter + 1
    }
    createSelect(counter)
}
const createSelect = (counter) => {
    const parentDiv = document.getElementById('paths')

    var heading = document.createElement("div");
    heading.innerHTML = "<h3>Select an option to view</h3>"
    parentDiv.appendChild(heading)

    var select = document.createElement("select");
    select.name = "Paths";
    select.id = "pathSelect"
    for (let i = 0; i < counter; i++) {
        const option = document.createElement('option')
        option.value = i
        option.text = i
        select.appendChild(option)
    }
    parentDiv.appendChild(select)
    // createButton
    let btn = document.createElement("button");
    btn.setAttribute('id', 'pathSubmitButton') 
    btn.innerHTML = "Animate Knight";
    btn.onclick = window.onPathSubmit
    parentDiv.appendChild(btn);

}

const createButton = () => {
    const parentDiv = document.getElementById('paths')
    const buttonDiv = document.createElement('div')
    const button = document.createElement('input')
    const text = document.createTextNode("Submit")
    button.setAttribute("onclick", () => {
        alert('$$$$$$$$$$')
    });
    button.setAttribute("type", 'submit');
    button.appendChild(text)
    buttonDiv.appendChild(button)
    parentDiv.appendChild(buttonDiv)
}

window.onPathSubmit = async () => {
    await globals.board.setPosition('empty')
    var e = document.getElementById("pathSelect");
    var pathValue = e.value;
    console.log('$$$$$$$$$$$$$$', pathValue)
    const selectedSolution = globals.solutions[pathValue]
    if (selectedSolution) {
        const firstElement = selectedSolution[0]
        globals.board.setPiece(firstElement, 'wn')
        for (const i in selectedSolution) {
            if (selectedSolution[parseInt(i) + 1]) {
                await globals.board.movePiece(selectedSolution[i], selectedSolution[parseInt(i)+1])
            }
        }
    }
}

window.getPaths = async (e) => {
    // e.preventDefault()
    const startX = document.getElementById('startX').value
    const startY = document.getElementById('startY').value
    const endX = document.getElementById('endX').value
    const endY = document.getElementById('endY').value
    if (!startX || !startY || !endX || !endY) {
        alert("all coordinates are required")
    } else if (startX === endX && startY === endY) {
        alert("cannot give same coordinates to both points")
    }
    const postBody = {
        start: [getNumberCoordinates(startX), getNumberCoordinates(startY)],
        end: [getNumberCoordinates(endX), getNumberCoordinates(endY)]
    }
    console.log(postBody)
    const resp = await postData(postBody)
    console.log(resp)
    globals.solutions = translatePaths(resp.solutions)
    renderPathsAsMap(globals.solutions)
    // return translatePaths(resp.solutions)
}

const translatePaths = (solutions) => {
    const numberToLetterMappingObj = swap(letterMapping)
    const numberToNumberMapping = swap(numberMapping)
    const newSolnsArray = []
    for (const solution of solutions) {
        const newPathArray = []
        const pathArray = solution.path
        for (const path of pathArray) {
            const newCoordinates = numberToLetterMappingObj[path[0]] + numberToNumberMapping[path[1]]
            newPathArray.push(newCoordinates)
        }
        newSolnsArray.push(newPathArray)
    }
    console.log(newSolnsArray)
    return newSolnsArray
}

function swap(json){
    var ret = {};
    for(var key in json){
        ret[json[key]] = key;
    }
    return ret;
}

const letterMapping = {
    a: 0,
    b: 1,
    c: 2,
    d: 3,
    e: 4,
    f: 5,
    g: 6,
    h: 7,
}

const numberMapping = {
    1: 0,
    2: 1,
    3: 2,
    4: 3,
    5: 4,
    6: 5,
    7: 6,
    8: 7
}

const getNumberCoordinates = (input) => {
    if (isNaN(parseInt(input))) {
        // is a string
        return letterMapping[input]
    } else {
        // is a number
        return numberMapping[input]
    }
}

async function postData(data = {}, url = 'http://127.0.0.1:5000/') {
    // Default options are marked with *
    const response = await fetch(url, {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        // mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin':'*'
            // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
}