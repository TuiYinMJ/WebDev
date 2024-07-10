function showModal() {
    // 获取模态框元素
    const modal = document.querySelector('.modal');

    // 显示模态框
    modal.style.display = 'block';

    // 焦点自动置入第一个输入框email
    modal.querySelector('input:first-of-type').focus();
}

function closeModal() {
    // 获取模态框元素
    const modal = document.querySelector('.modal');

    // 关闭模态框
    modal.style.display = 'none';
}