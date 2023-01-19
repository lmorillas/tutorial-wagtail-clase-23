new Glide(
    '[data-component="hero"]',
    {
        focusAt: "center", startAt: 7, perView: 6, peek: 50, gap: 30, autoplay: 2500, hoverpause: !1,
        animationDuration: 1e3, rewindDuration: 2e3, touchRatio: .25, perTouch: 1,
        breakpoints: {
            480: { gap: 15, peek: 75, perView: 1 }, 768: { perView: 2 },
            1360: { perView: 3 }, 1600: { perView: 4 }, 1960: { perView: 5 }
        }
    })
    .mount({
        Coverflow: function (e, t, n) {
            var i = {
                tilt: function (e) {
                    e.querySelector(c).style.transform = "perspective(1500px) rotateY(0deg)",
                    this.tiltPrevElements(e), this.tiltNextElements(e)
                },
                tiltPrevElements: function (e) {
                    for (var t = function (e) {
                        var t = []; if (e) for (; e = e.previousElementSibling;)
                            t.push(e); return t
                    }(e), n = 0; n < t.length; n++) { var i = t[n].querySelector(c); i.style.transformOrigin = "100% 50%", i.style.transform = "perspective(1500px) rotateY(".concat(20 * Math.max(n, 2), "deg)") }
                }, tiltNextElements: function (e) { for (var t = function (e) { var t = []; if (e) for (; e = e.nextElementSibling;)t.push(e); return t }(e), n = 0; n < t.length; n++) { var i = t[n].querySelector(c); i.style.transformOrigin = "0% 50%", i.style.transform = "perspective(1500px) rotateY(".concat(-20 * Math.max(n, 2), "deg)") } }
            }; return n.on(["mount.after", "run"], (function () { i.tilt(t.Html.slides[e.index]) })), i
        }
    });
