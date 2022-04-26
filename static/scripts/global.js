const afterInsertHeader = () => {
  for (const anchor of document.querySelectorAll("#header-page-list > a")) {
    if (anchor.href === window.location.href) {
      anchor.classList.add("header-link-current-page");
    }
  }
};

fetch("/header.html")
  .then((res) => res.text())
  .then((headerHtml) => {
    document.body.insertAdjacentHTML("afterbegin", headerHtml);
    afterInsertHeader();
  });
