function triggerDefault() {
    submitText();
    getTokens();
}

function submitText() {
    var inputText = document.getElementById("inputText").value
    var payload = { text: inputText };
    scoreAPI(JSON.stringify(payload))
    console.log(inputText);
}

function scoreAPI(payload) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/score");
    xhr.setRequestHeader("content-type", "application/json");
    xhr.setRequestHeader("cache-control", "no-cache");

    xhr.addEventListener("readystatechange", function () {
        if (this.readyState === 4 && this.status == 200) {
            console.log(this.responseText);
            updateScore(JSON.parse(this.responseText))
        }
        else {
            console.log(this.responseText)
        }
    });

    xhr.send(payload);
}

function updateScore(response) {
    // update score card
    var score = "Difficulty score is " + response["score"];
    document.getElementById("scoreBoard").innerHTML = score;

    // update word categories
    var htmlList = document.getElementById("easyWords");
    var data = response["words"]["easy"];
    updateList(htmlList, data);

    htmlList = document.getElementById("mediumWords");
    data = response["words"]["medium"];
    updateList(htmlList, data);

    htmlList = document.getElementById("hardWords");
    data = response["words"]["hard"];
    updateList(htmlList, data);
}

function updateList(htmlList, data) {
    htmlList.innerHTML = '';
    for (i = 0; i < data.length; i++) {
        item = document.createElement('li');
        item.setAttribute("class", "list-group-item");
        item.innerHTML = data[i];
        htmlList.appendChild(item);
    }
    if (data.length > 10) {
        htmlList.style.maxHeight = "400px";
        htmlList.style.overflowY = "auto";
    }
}

function getTokens() {
    var input = document.getElementById("inputText").value
    var word_count = 0;
    var sentence_count = 0;
    for (i = 0; i < input.length; i++) {
        if (input[i] == ' ') {
            word_count += 1;
        }
        if (input[i] == '.') {
            sentence_count += 1;
        }
    }
    document.getElementById("wordCount").textContent = word_count + 1;
    document.getElementById("sentenceCount").textContent = sentence_count;
}