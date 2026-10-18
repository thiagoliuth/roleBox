(() => {
    const buttons = document.querySelectorAll("[data-theme-toggle]");

    function updateButtons(theme) {
        const nextTheme = theme === "dark" ? "light" : "dark";
        buttons.forEach((button) => {
            button.setAttribute("aria-label", `Ativar tema ${nextTheme === "light" ? "claro" : "escuro"}`);
        });
    }

    let currentTheme = document.documentElement.dataset.theme;
    updateButtons(currentTheme);

    buttons.forEach((button) => {
        button.addEventListener("click", () => {
            currentTheme = currentTheme === "dark" ? "light" : "dark";
            document.documentElement.dataset.theme = currentTheme;
            try {
                localStorage.setItem("partyboxd-theme", currentTheme);
            } catch (_) {}
            updateButtons(currentTheme);
        });
    });

})();
