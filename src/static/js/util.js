function sleep(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
}

async function redirect(url, s) {
    await sleep(s * 1000);
    console.log("Redirecting to " + url + "...");
    window.location.replace(url);
}