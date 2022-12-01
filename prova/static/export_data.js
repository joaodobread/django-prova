function exportData(formId) {
    const form = document.getElementById(formId);
    if (!form.checkValidity())
        return alert(
            "Valores inválidos, preencha corretamente o formulário para exportar."
        );
    const prevAction = form.action;
    form.action = "/clientes/export";
    form.submit();
    form.action = prevAction;
}
