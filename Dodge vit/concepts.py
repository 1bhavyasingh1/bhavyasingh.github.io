.css
.gameContainer {
    background-image: url(vit.png);
    background-repeat: no-repeat;
    background-size: 100vw 100vh;
    width: 100%;
    height: 100vh;
}
Removing background-size: 100vw 100vh;
the image doesn't over the whole page







.css
.BCE {
    background-image: url(BCE.png);
    background-repeat: no-repeat;
    background-size: cover;
    width: 100px;
    height: 100px;
    position: absolute;
    bottom: 0;
    left: 12px;
}
width: 100px;
    height: 100px;   makes it a small square

position: absolute;
    bottom: 0;       brings it to the bottom-left

    left: 52px;      shifts it slightly to the right






 .js   
if (e.keyCode == 38) {
      BCE = document.querySelector('.BCE');
} 
instead you can do BCE = document.getElementById






.js
BCE.classList.add('animateBCE');
I will jump using this
    
setTimeout(() => {
    BCE.classList.remove('animateBCE')
}, 700);
Using this the jump animation will stop in 700ms






.css
@keyframes obstacleAni {
    0% {
        left: 100vw;
    }

    100% {
        left: -10vw;
    }
}
Removing any 1 of those slows vishu down





.css
body {
    background-color: red;
    overflow: hidden;
}
overflow: hidden; was to get rid of the horizontal scrollbar that kept coming after vishu left the frame







.js
setInterval(() => {
      This means keep doing it for every 100ms 
}, 100);







.js
gameOver = document.querySelector('.gameOver');
gameOver came from the html file
<div class="gameOver"> 0 cgpa</div>





.js
dx = window.getComputedStyle(BCE, null).getPropertyValue('left');
Will give us the x axis value of 'BCE'
dy = window.getComputedStyle(BCE, null).getPropertyValue('top');
Will give us the y axis value of 'BCE'
ox = window.getComputedStyle(obstacle, null).getPropertyValue('left');
oy = window.getComputedStyle(obstacle, null).getPropertyValue('top');
Will give the x and y axis of vishu







offsetx = Math.abs(dx - ox);
The distance between you and vishu on the x-axis
offsety = Math.abs(dy - oy);
The distance between you and vishu on the y-axis







.css
.gameOver {
    visibility: hidden;
}
.js
if (offsetx < 93 && offsety < 52) {
        gameOver.style.visibility = 'visible';
    }
so it will only be visible when it collides







.js
dx = parseInt(window.getComputedStyle(BCE, null).getPropertyValue('left'));
    dy = parseInt(window.getComputedStyle(BCE, null).getPropertyValue('top'));

    ox = parseInt(window.getComputedStyle(obstacle, null).getPropertyValue('left'));
    oy = parseInt(window.getComputedStyle(obstacle, null).getPropertyValue('top'));

The "parseInt" function was used to conver the px(pixel) values to integer so that the condition
if (offsetx < 93 && offsety < 52) {
        gameOver.style.visibility = 'visible';
        obstacle.classList.remove('obstacleAni')
    }
so that (offsetx < 93 && offsety < 52) this condition can be used for "gameOver"










 if (e.keyCode == 39) {
        BCE = document.querySelector('.BCE');
        BCEx = parseInt(window.getComputedStyle(BCE, null).getPropertyValue('left'));
        BCE.style.left = BCEx + 112 + "px";
    }
was to enable the forward arrow key







if (e.keyCode == 37) {
        BCE = document.querySelector('.BCE');
        BCEx = parseInt(window.getComputedStyle(BCE, null).getPropertyValue('left'));
        BCE.style.left = BCEx - 112 + "px";
    }
The only difference between the left and right key is right key has "+112" and left key has "-112".   







score = 0;
cross = true;

else if (cross && offsetx < 145) {
        score += 1;
        updateScore(score);
        cross = false;
        setTimeout(() => {
            cross = true;
        }, 1000)
    }
all these are used to increase the score 
"offsetx < 145" condition states that vishu should be close to you on the x-axis  







aniDur = parseFloat(window.getComputedStyle(obstacle, null).getPropertyValue('animation-duration'));
        newDur = aniDur - 0.1;
        obstacle.style.animationDuration = newDur + 's';
This will increase the velocity of vishhu        