
let map = document.querySelector('.map');
let page = document.querySelector('.home-page');
let map_img = document.querySelector('#map-png');
map_img.addEventListener("mousemove", getPos);
map_img.addEventListener("click", async (e) => {
    const pos = getPos(e);
    const depth = await getDepth(lat, long);
    window.location.href = `/dive?lat=${pos.lat}&long=${pos.long}&depth=${depth}`;
});

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
    return {lat: lat,
        long: long
    }
}


 async function getDepth(lat, long) {
    resp = await fetch(`https://ocean.amentum.io/gebco?latitude=${lat}&longitude=${long}`, {
        method: "GET",
        headers: {
        "accept": "application/json",
        "API-Key": "M49Fwt5v69bSrPkEALthhA180ydLqcAq"
        }
    })
    res = await resp.json();
    console.log(res);
    return res.elevation.value;
    
    }

