// The line on the front page that turns through the ten ideas of a ghost.
// Without this script the first one simply stays put.
(function () {
  var turn = document.querySelector("[data-turn]");
  if (!turn) return;

  var phrase = turn.querySelector("[data-turn-phrase]");
  var by = turn.querySelector("[data-turn-by]");
  var toggle = turn.querySelector("[data-turn-toggle]");
  var items = Array.prototype.slice.call(turn.querySelectorAll(".turn-source li"));
  if (items.length < 2) return;

  var stillPlease = window.matchMedia("(prefers-reduced-motion: reduce)");
  var index = 0;
  var timer = null;
  var paused = false;

  // The dark picture behind the title changes with the line. Two layers
  // take turns, so no more than two pictures are ever held at once. A
  // writer with no picture yet leaves the plate plain.
  var layers = Array.prototype.slice.call(document.querySelectorAll("[data-turn-plate] img"));
  var front = 0;

  function showPicture(i) {
    if (layers.length < 2) return;
    var set = items[i].getAttribute("data-ghost");
    var incoming = layers[1 - front];
    var outgoing = layers[front];
    front = 1 - front;
    function swap() {
      if (layers[front] !== incoming) return;
      incoming.classList.add("is-shown");
      outgoing.classList.remove("is-shown");
    }
    if (!set) {
      incoming.classList.remove("is-shown");
      outgoing.classList.remove("is-shown");
      return;
    }
    incoming.onload = swap;
    incoming.setAttribute("srcset", set);
    if (incoming.complete && incoming.naturalWidth) swap();
  }

  function show(i) {
    showPicture(i);
    phrase.innerHTML = items[i].innerHTML;
    by.textContent = items[i].getAttribute("data-by");
    turn.style.setProperty("--accent", items[i].getAttribute("data-accent"));
    turn.style.setProperty("--accent-night", items[i].getAttribute("data-accent-night"));
  }

  function next() {
    turn.classList.add("is-changing");
    window.setTimeout(function () {
      index = (index + 1) % items.length;
      show(index);
      turn.classList.remove("is-changing");
    }, 650);
  }

  function start() {
    if (timer || paused || stillPlease.matches || document.hidden) return;
    timer = window.setInterval(next, 4800);
  }

  function stop() {
    window.clearInterval(timer);
    timer = null;
  }

  // People who ask for less motion get a button to step through instead.
  if (stillPlease.matches) {
    toggle.textContent = "Next";
    toggle.removeAttribute("aria-pressed");
    toggle.addEventListener("click", function () {
      index = (index + 1) % items.length;
      show(index);
    });
  } else {
    toggle.addEventListener("click", function () {
      paused = !paused;
      toggle.textContent = paused ? "Play" : "Pause";
      toggle.setAttribute("aria-pressed", paused ? "true" : "false");
      if (paused) stop(); else start();
    });
  }
  toggle.hidden = false;

  document.addEventListener("visibilitychange", function () {
    if (document.hidden) stop(); else start();
  });
  start();
})();
