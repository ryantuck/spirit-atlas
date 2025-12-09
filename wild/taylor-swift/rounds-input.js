var roundsInput = document.getElementById('rounds');
roundsInput.addEventListener('input', () => {
    // input = 2, take divs[6:]
    // input = 5, take divs[3:]
    // input = 8, take divs[0:]
    // nth-child display none
    //
    var bracketDiv = document.querySelector('.bracket');
    var roundElements = bracketDiv.querySelectorAll(":scope > div");
    var startingIdx = 7 - roundsInput.value;

    console.log(roundElements);

    for (var i = 0; i < roundElements.length; i++) {

        if (i < startingIdx) {
            roundElements[i].classList.remove("bracket-round");
            roundElements[i].classList.add("c");
            roundElements[i].style.display = "none";

        }
        else {

            roundElements[i].classList.remove("c");
            roundElements[i].classList.add("bracket-round");
            roundElements[i].style.display = "flex";
            roundElements[i].style.setProperty('flex-basis', 1);

            var nCols = 7 - startingIdx;
            var relIdx = i-startingIdx;

            var fontSizes = [0.5, 0.6, 1.0, 1.1, 1.2, 1.3, 1.5];
            var fontVar = fontSizes[relIdx];

            roundElements[i].style.fontSize = fontVar.toString() + 'rem';

            const h = 4 * Math.pow(2,relIdx);
            const subdivs = roundElements[i].querySelectorAll('div');
            subdivs.forEach(d => d.style.height = h.toString()+'vh');
            subdivs[0].style.height = (2 + h/2).toString()+ 'vh';
            subdivs.forEach(d => d.style.fontSize = fontVar.toString() + 'rem');

        }
    }
    document.getElementById('nRounds').innerText = Math.pow(2, roundsInput.value-1);
});
