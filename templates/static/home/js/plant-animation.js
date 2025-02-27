var animDuration = 5;
var leafAnimDuration = 2;
var animDurationPart = animDuration / 27; //Leaf number
var leavesTransOrigin = ['0% 50%','100% 100%','0% 50%','80% 0%','0% 0%','100% 0%','50% 0%','100% 100%','0% 50%',
'100% 90%','50% 100%','100% 100%','100% 50%','30% 0%','100% 0%','100% 90%','0% 0%','100% 80%','50% 0%',
'0% 0%','100% 50%','100% 60%','0% 0%','80% 20%','0% 0%','100% 0%','10% 10%'];

var leavesTransOriginS = ['0% 50%','100% 0%','0% 50%','80% 100%','0% 100%','100% 100%','50% 100%','100% 0%','0% 50%',
'100% 10%','50% 0%','100% 0%','100% 50%','30% 100%','100% 100%','100% 10%','0% 100%','100% 20%','50% 100%',
'0% 100%','100% 50%','100% 40%','0% 100%','80% 80%','0% 100%','100% 100%','10% 90%'];

var origMain = document.querySelector('#mainBranch');
var objMain = {length:0,
           pathLength:origMain.getTotalLength()};

function drawLineMain() {
  origMain.style.strokeDasharray = [objMain.length,objMain.pathLength].join(' ');
}

TweenMax.to(objMain, animDuration, {length:objMain.pathLength, strokeWidth:30, onUpdate:drawLineMain, ease:Sine.easeOut});

var origShadow = document.querySelector('#shadowBranch');
var objShadow = {length:0, pathLength:origShadow.getTotalLength()};

function drawLineShadow() {
  origShadow.style.strokeDasharray = [objShadow.length,objShadow.pathLength].join(' ');
}

TweenMax.to(objShadow, animDuration, {length:objShadow.pathLength, strokeWidth:30, onUpdate:drawLineShadow, ease:Sine.easeOut});

for(var i = 0; i < 27; i++){
  TweenMax.from('#leaf' + (i + 1), Math.random() + leafAnimDuration, {scale: 0, 
                                                                      transformOrigin:leavesTransOrigin[i], delay:animDurationPart * i});
  TweenMax.from('#leafS' + (i + 1), Math.random() + leafAnimDuration, {scale: 0, transformOrigin:leavesTransOriginS[i], delay:animDurationPart * i});
}

var tlFallingleaf = new TimelineMax();
tlFallingleaf.delay(animDuration + leafAnimDuration).
              to('#leaf25', .5, {rotation:7, ease:Linear.easeInOut}).
              to('#leaf25', .4, {rotation:2, ease:Linear.easeInOut}).
              to('#leaf25', .3, {rotation:7, ease:Linear.easeInOut}).
              to('#leaf25', .2, {rotation:5, ease:Linear.easeInOut}).
              to('#leaf25', 1.5, {y:'+=960', rotation:90, transformOrigin:'50% 50%', ease:Linear.easeOut}).
              to('#leaf25', .5, {rotation:80, transformOrigin:'70% 50%', ease:Linear.easeNone}).
              to('#leaf25', .3, {rotation:85, transformOrigin:'70% 50%', ease:Linear.easeNone});

var tlFallingleafS = new TimelineMax();
tlFallingleafS.delay(animDuration + leafAnimDuration + 1.4).
              to('#leafS25', 1.5, {y:'-=960', rotation:-90, transformOrigin:'50% 50%', ease:Linear.easeOut}).
              to('#leafS25', .5, {rotation:-80, transformOrigin:'70% 50%', ease:Linear.easeNone}).
              to('#leafS25', .3, {rotation:-85, transformOrigin:'70% 50%', ease:Linear.easeNone});

var tlShadow = new TimelineMax();
tlShadow.delay(animDuration + leafAnimDuration + 1.4).
              staggerFrom('#leafShadow', 1.5, {scale:0, transformOrigin:'50% 50%', ease:Linear.easeNone}).
              staggerTo('#leafShadow', .5, {scale:1.1, transformOrigin:'50% 50%', ease:Linear.easeNone}).
              staggerTo('#leafShadow', .3, {scale:1, transformOrigin:'50% 50%', ease:Linear.easeNone});

var tlRipple = new TimelineMax();
tlRipple.delay(animDuration + leafAnimDuration + 2.7).
              from('#leafRipple', .4, {scale:0, transformOrigin:'50% 50%', ease:Linear.easeIn}).
              to('#leafRipple', .4, {scale:2, opacity:0, ease:Linear.easeOut});


