document.getElementById("uploadForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    let formData = new FormData();
    formData.append("eye", document.getElementById("eye").files[0]);
    formData.append("skin", document.getElementById("skin").files[0]);
    formData.append("nail", document.getElementById("nail").files[0]);

    try {
        let response = await fetch("/predict", {
            method: "POST",
            body: formData,
        });

        let data = await response.json();
        if (data.error) {
            document.getElementById("result").innerHTML = `<p class="error">${data.error}</p>`;
        } else {
            let resultHTML = "<h3>Top 2 Deficiencies:</h3><ul>";
            data.top_2_deficiencies.forEach((item) => {
                resultHTML += `<li><strong>${item.vitamin}</strong>: ${item.diseases.join(", ")}</li>`;
            });
            resultHTML += "</ul>";
            document.getElementById("result").innerHTML = resultHTML;
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerHTML = `<p class="error">Error sending request to server.</p>`;
    }
});
