async function fetchSuggestions() {
    const input = document.getElementById("address").value;
    const suggestionsList = document.getElementById("suggestions");
    suggestionsList.innerHTML = ""; // Clear previous results

    if (input.length < 3) return; // Fetch after 3+ characters

    const apiKey = "9048966996da4ac395098eef17315ec5"; // Replace with your real API key
    const url = `https://api.opencagedata.com/geocode/v1/json?q=${input}&key=${apiKey}&limit=5`;

    try {
        const response = await fetch(url);
        const data = await response.json();

        if (data.results.length > 0) {
            data.results.forEach((result) => {
                const li = document.createElement("li");
                li.textContent = result.formatted;
                li.onclick = () => {
                    document.getElementById("address").value = result.formatted;
                    suggestionsList.innerHTML = ""; // Clear suggestions after selection
                };
                suggestionsList.appendChild(li);
            });
        }
    } catch (error) {
        console.error("Error fetching suggestions:", error);
    }
}
