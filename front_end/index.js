// Input matrix
document.getElementById("solve-button").addEventListener("click", execute_operation)

function execute_operation(){
    const inputField = document.getElementById("input-text");
    const inputText = inputField.value;

    if (inputText === '') {
        return;
    }

    const selectOperation = document.getElementById("operation-to-do");
    const operation = selectOperation.value;

    if (operation === "multiply") {

    } else if (operation === "invert") {

    } else {

    }

}

function multiply(m1, m2) {
    let result = Array.from({ length: m1.length }, () => Array(m2[0].length).fill(0));

    for (let i = 0; i < m1.length; i++) {
        for (let j = 0; j < m2[0].length; j++) {
            for (let k = 0; k < m2.length; k++) {
                result[i][j] += m1[i][k] * m2[k][j];
            }
        }
    }

    return result;
}

function invert(matrix) {
    // TODO: Check every row for the correct amount of values (square matrix)

    let n = matrix.length;

    let identityMatrix = Array.from({ length: n }, (_, j) => 
        Array.from({ length: n }, (_, i) => (i === j ? 1.0 : 0.0))
    );

    let augmented_matrix = Array.from({length: n}, (_, j) =>
        from({length: n}, (_,i) => (i === j ? 1.0 : 0.0))
    );

    for (let i = 0; i < n; i++) {
        if (augmented_matrix[i][i] === 0) {
            for (let j = i + 1; j < n; j++) {
                // Swap rows
                let temp = augmented_matrix[i];
                augmented_matrix[i] = augmented_matrix[j];
                augmented_matrix[j] = temp;
                break;
            }

            throw new Error("Matrix is singular and can't be inverted");
        }

        // Normalize the row by dividing by the diagonal element
        let diagonal_elem = augmented_matrix[i][i];
        for (let j = 0; j < 2 * n; j++) {
            augmented_matrix[i][j] = augmented_matrix[i][j] / diagonal_elem;
        }

        // Remove all other elements in the current column
        for (let j = 0; j < n; j++) {
            if (i != j) {
                let ratio = augmented_matrix[j][i];

                for (let k = 0; k < 2 * n; k++) {
                    augmented_matrix[j][k] = augmented_matrix[j][k] - (ratio * augmented_matrix[i][k])
                    augmented_matrix[j][k] = augmented_matrix[j][k].tofixed(5); // Round to 5 decimal places
                }
            }
        }
    }

    let inverse_matrix = augmented_matrix.map(row => row.slice(n));

    return inverse_matrix
}
