function randomMap() {
    // 先调用clearCubes函数来清除上一次在场景中添加的立方体
    clearCubes();
    // 再调用createCubes函数来创建新的立方体
    createCubes();
}
function clearCubes() {
    // 遍历数组中的每个立方体对象
    for(var i = 0; i < cubes.length; i++){
        // 获取当前立方体对象
        var cube = cubes[i];
        // 在其父对象上调用scene.remove方法
        cube.parent.remove(cube);
        // 调用renderer.renderLists.dispose()方法
        renderer.dispose();
    }
    // 清空数组
    cubes = [];
    graph = [];
}
function createCubes() {
    // 创建一个名为cubes的数组，用于存储所有的立方体对象
    var geometry = new THREE.CubeGeometry(9, 9, 9);
    var material = new THREE.MeshBasicMaterial({
        color: 0xC0C0C0
    });
    for(var i = 0; i < length / 10; i++){
        var nodeRow = [];
        graph.push(nodeRow);
        for(var j = 0; j < length / 10; j++){
            var salt = randomNum(1, 7);
            if (salt > flex) nodeRow.push(1);
            else nodeRow.push(0);
            if (salt <= flex) {
                var cube = new THREE.Mesh(geometry, material);
                cube.position.set(10 * j - length / 2 + 5, 5, 10 * i - length / 2 + 5);
                scene.add(cube);
                // 将立方体对象添加到数组中
                cubes.push(cube);
            }
        }
    }
}

//# sourceMappingURL=index.52f2910e.js.map
