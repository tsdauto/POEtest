document.addEventListener('contextmenu', function(event) {
    // event.preventDefault();
    const element = event.target;
    const selector = getUniqueSelector(element);
    console.log(selector);

    copyToClipboard(selector);
});

function getUniqueSelector(el) {
    if (!(el instanceof Element)) return '';
    const path = [];
    while (el) {
        let selector = el.nodeName.toLowerCase();
        if (el.id) {
            selector = `#${el.id}`;
            path.unshift(selector);
            break;
        } else {
            let sib = el, nth = 1;
            while (sib.previousElementSibling) {
                sib = sib.previousElementSibling;
                if (sib.nodeName.toLowerCase() === selector) nth++;
            }
            if (nth !== 1) selector += `:nth-child(${nth})`;
        }
        path.unshift(selector);
        el = el.parentElement;
    }
    return path.join(' > ');
}

function copyToClipboard(text) {

    if (navigator.clipboard) {
        navigator.clipboard.writeText(text)
            .then(() => console.log('CSS selector copied to clipboard!'))
            .catch(err => console.error('Clipboard API failed: ', err));
    } else {

        try {
            const textarea = document.createElement('textarea');
            textarea.value = text;
            textarea.style.position = 'fixed'; // 避免影響頁面
            document.body.appendChild(textarea);
            textarea.focus();
            textarea.select();
            const successful = document.execCommand('copy');
            document.body.removeChild(textarea);
            if (successful) {
                console.log('CSS selector copied to clipboard (fallback method)!');
            } else {
                console.error('Failed to copy using fallback method.');
            }
        } catch (err) {
            console.error('Fallback copy failed: ', err);
        }
    }
}