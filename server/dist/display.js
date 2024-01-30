function displayLogin(callback) {
    $("body").append(`<div class="login">
        <div class="input_container">
            <label>Saisissez le code de connexion : </label>
            <input class="uuid_input" type="text" placeholder="2d04d26f-faad-4d35-a1b0-b24355e7ac7d">
        </div>
    </div>`);

    const $input = $(".uuid_input");
    $input.on("keydown keyup", e => {
        if (e.keyCode === 13) {
            callback($input.val());
        }
    });
}

function displayConfig(configList, callback) {
    $(".login").hide();

    $("body").append(`<div class="handler_container">`);
    const $handler_container = $(".handler_container");
    configList.forEach(handler => {
        const $button = $(`<div class="handler_button" id="handler_button_${handler.id}">
            <span>${handler.name} : </span>
            <span class="handler_value">[${handler.value}]</span>
        </div>`);
        $handler_container.append($button);
        const $sub_container = $(`<div class="sub_container"></div>`);
        $handler_container.append($sub_container);

        handler["sub-cells"].forEach(sub => {
            const $subButton = $(`<div class="handler_sub_button" id="handler_sub_button_${sub.id}">
                <span>${sub.name} : </span>
                <span>[${sub.value}]</span>
            </div>`);
            $subButton.on("click", _ => {
                console.log(handler, sub);
                callback(handler.id, sub.value);
            });
            $sub_container.append($subButton);
        });
    });
}

function updateConfig(data) {
    if (data.error)  {
        console.log("ERROR");
        return
    }
    $(`#handler_button_${data.id} .handler_value`).text(`[${data.value}]`);
}