function buildTable(rows) {
    const table = document.getElementById("result");
    table.innerHTML = "";

    if (!rows.length) return;


    // fill header
    tr = table.insertRow(-1);
    Object.keys(rows[0]).forEach((val) => {
        var th = document.createElement("th"); // TABLE HEADER.
        th.innerHTML = val;
        tr.appendChild(th);
    });

    // fill rows
    for (let index = 0; index < rows.length; index++) {
        const row = rows[index];

        tr = table.insertRow(-1);

        Object.values(row).forEach((val) => {
            const tabCell = tr.insertCell(-1);
            tabCell.innerHTML = val;
        });
    }
}