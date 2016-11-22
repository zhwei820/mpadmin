## 创建层

**接口地址：**

> BASE_URL/arch/layer/create/

**请求方法：**

POST

**请求参数：**

    {
        "name": "create_layer1"
    }

**参数说明：**

> name: string, 层名字，需要保证唯一性

**返回结果示例：**

成功：

    http status 201
    
    {
        "id": "5833a9251774d5078c6bd18f",
        "name": "create_layer1"
    }

## 修改层

**接口地址：**

> BASE_URL/arch/layer/(id)/update/

**请求方法：**

PUT

**请求参数：**

    {
        "name": "create_layer1"
    }

**参数说明：**

> name: string, 层名字，需要保证唯一性

**返回结果示例：**

成功：

    http status 200
    
    {
        "id": "5833a9251774d5078c6bd18f",
        "name": "create_layer1"
    }

## 查看具体层

**接口地址：**

> BASE_URL/arch/layer/(id)/

**请求方法：**

GET

**返回结果示例：**

成功：

    http status 200
    
    {
        "id": "5833a9251774d5078c6bd18f",
        "name": "create_layer5"
    }

## 查看所有层

**接口地址：**

> BASE_URL/arch/layer/list/

**请求方法：**

GET

**返回结果示例：**

成功：

    http status 200
    
    [
        {
            "id": "583285cb1774d50ea85802f8",
            "name": "create_layer1"
        },
        {
            "id": "5833a9251774d5078c6bd18f",
            "name": "create_layer3"
        }
    ]
    
## 删除层
    
**接口地址：**

> BASE_URL/arch/layer/(id)/

**请求方法：**

DELETE

**返回结果示例：**

成功：

    http status 204

## 创建组

**接口地址：**

> BASE_URL/arch/group/create/

**请求方法：**

POST

**请求参数：**

    {
        "name": "create_group1",
        "layer": "583285cb1774d50ea85802f8"
    }

**参数说明：**

> name: string, 组名字，需要和layer保证联合唯一性
> layer: string(24位), 所属层ID

**返回结果示例：**

成功：

    http status 201
    
    {
        "id": "5833a9251774d5078c6bd18f",
        "name": "create_layer1",
        "layer": "583285cb1774d50ea85802f8"
    }

## 修改组

**接口地址：**

> BASE_URL/arch/group/(id)/update/

**请求方法：**

PUT

**请求参数：**

    {
        "name": "create_layer1",
        "layer": "583285cb1774d50ea85802f8"
    }

**参数说明：**

> name: string, 组名字，需要和layer保证联合唯一性
> layer: string(24位), 所属层ID

**返回结果示例：**

成功：

    http status 200
    
    {
        "id": "5833a9251774d5078c6bd18f",
        "name": "create_layer1",
        "layer": "583285cb1774d50ea85802f8"
    }

## 查看具体组

**接口地址：**

> BASE_URL/arch/group/(id)/

**请求方法：**

GET

**返回结果示例：**

成功：

    http status 200
    
    {
        "id": "5833a9251774d5078c6bd18f",
        "name": "create_layer1",
        "layer": "583285cb1774d50ea85802f8"
    }

## 查看某一层的所有组

**接口地址：**

> BASE_URL/arch/group/(id)/

**请求方法：**

GET

**参数说明：**

>id: 层ID

**返回结果示例：**

成功：

    http status 200
    
    [
        {
            "id": "583285cb1774d50ea85802f8",
            "name": "create_group1"
        },
        {
            "id": "5833a9251774d5078c6bd18f",
            "name": "create_group3"
        }
    ]
    
## 删除组
    
**接口地址：**

> BASE_URL/arch/group/(id)/

**请求方法：**

DELETE

**返回结果示例：**

成功：

    http status 204