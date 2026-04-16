const topbar = document.querySelector(".topbar");
const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelectorAll(".nav a");
const revealItems = document.querySelectorAll(".reveal");
const heroFrame = document.querySelector(".hero-media-frame");
const heroBackdrop = document.querySelector(".hero-media-backdrop");
const heroCard = document.querySelector(".hero-detail-card");
const animatedGroups = document.querySelectorAll(".about-panel, .service-card, .course-card, .why-feature, .why-quote");

document.body.classList.add("is-ready");

animatedGroups.forEach((item, index) => {
  item.setAttribute("data-reveal-delay", String(index % 4));
});

if (menuToggle && topbar) {
  menuToggle.addEventListener("click", () => {
    const isOpen = topbar.classList.toggle("menu-open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      topbar.classList.remove("menu-open");
      menuToggle.setAttribute("aria-expanded", "false");
    });
  });
}

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        revealObserver.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.16,
    rootMargin: "0px 0px -40px 0px",
  }
);

revealItems.forEach((item) => {
  revealObserver.observe(item);
});

if (heroFrame && heroBackdrop && heroCard && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  heroFrame.addEventListener("pointermove", (event) => {
    const bounds = heroFrame.getBoundingClientRect();
    const x = (event.clientX - bounds.left) / bounds.width - 0.5;
    const y = (event.clientY - bounds.top) / bounds.height - 0.5;

    heroFrame.style.transform = `rotateX(${y * -2.6}deg) rotateY(${x * 3.8}deg) translateY(-4px)`;
    heroBackdrop.style.transform = `scale(1.1) translate3d(${x * -14}px, ${y * -12}px, 0)`;
    heroCard.style.transform = `translate3d(${x * 10}px, ${y * 10}px, 0)`;
  });

  heroFrame.addEventListener("pointerleave", () => {
    heroFrame.style.transform = "";
    heroBackdrop.style.transform = "";
    heroCard.style.transform = "";
  });
}
