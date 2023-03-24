score = 0;
cross = true;


audio = new Audio('tamil.mp3');
document.onkeydown = function (e) {
    console.log("Key code is: ", e.keyCode)
    if (e.keyCode == 38) {
        BCE = document.querySelector('.BCE');
        BCE.classList.add('animateBCE');
        setTimeout(() => {
            BCE.classList.remove('animateBCE')
        }, 700);
    }
    if (e.keyCode == 39) {
        BCE = document.querySelector('.BCE');
        BCEx = parseInt(window.getComputedStyle(BCE, null).getPropertyValue('left'));
        BCE.style.left = BCEx + 112 + "px";
    }
    if (e.keyCode == 37) {
        BCE = document.querySelector('.BCE');
        BCEx = parseInt(window.getComputedStyle(BCE, null).getPropertyValue('left'));
        BCE.style.left = BCEx - 112 + "px";
    }
}




setInterval(() => {
    BCE = document.querySelector('.BCE');
    gameOver = document.querySelector('.gameOver');
    obstacle = document.querySelector('.obstacle');

    dx = parseInt(window.getComputedStyle(BCE, null).getPropertyValue('left'));
    dy = parseInt(window.getComputedStyle(BCE, null).getPropertyValue('top'));

    ox = parseInt(window.getComputedStyle(obstacle, null).getPropertyValue('left'));
    oy = parseInt(window.getComputedStyle(obstacle, null).getPropertyValue('top'));

    offsetx = Math.abs(dx - ox);
    offsety = Math.abs(dy - oy);
    console.log(offsetx, offsety)
    if (offsetx < 73 && offsety < 52) {
        gameOver.style.visibility = 'visible';
        obstacle.classList.remove('obstacleAni')
        audio.play();
        setTimeout(() => {
            audio.pause();
        })
    }
    else if (cross && offsetx < 145) {
        score += 1;
        updateScore(score);
        cross = false;
        setTimeout(() => {
            cross = true;
        }, 1000)
        setTimeout(() => {
            aniDur = parseFloat(window.getComputedStyle(obstacle, null).getPropertyValue('animation-duration'));
            newDur = aniDur - 0.8;
            obstacle.style.animationDuration = newDur + 's';
            console.log('New animation duration', newDur)
        }, 500)

    }

}, 100);


function updateScore(score) {
    scoreCont.innerHTML = "Your Score: " + score
}