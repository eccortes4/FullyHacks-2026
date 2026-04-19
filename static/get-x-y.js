
let map = document.querySelector('.map');
let page = document.querySelector('.home-page');
let map_img = document.querySelector('#map-png')
map_img.addEventListener("mousemove", getPos)

function getPos(e) {
    const map_x = map_img.getBoundingClientRect().x;
    const map_y = map_img.getBoundingClientRect().y;
    const map_width = map_img.getBoundingClientRect().width;
    const map_height = map_img.getBoundingClientRect().height;

    x=e.clientX - map_x;
    y=e.clientY - map_y;

    rel_x = x / map_width;
    rel_y = y / map_height;

    long = -195 + 65 * rel_x
    lat = 45 - 45 * rel_y 

    cursor=`Your Mouse Position Is : ${lat} and  ${long}`;
    document.getElementById("coords").innerText=cursor
}

