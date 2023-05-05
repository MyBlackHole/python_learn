from typing import Optional, Tuple

from kazoo.client import KazooClient

# path = "/udal_cluster/tenant_1/hosts/host_0000000013"
# data: Optional[Tuple] = zk.get(path)
# print(data)


def print_node_all_childs(zk_client: KazooClient, child_path: str):
    data: Optional[Tuple] = zk_client.get(child_path)
    if data:
        print("child_path", child_path)
        try:
            print("data", data[0].decode())
        except Exception as e:
            print("data", data[0])
        print("ZnodeStat", data[1])
        print("*" * 20)

    child_nodes = zk_client.get_children(child_path) or []
    for child in child_nodes:
        path = child_path + "/" + child
        print_node_all_childs(zk, path)


if __name__ == "__main__":
    status = True
    start_path = "/teledb"
    zk = KazooClient(hosts="192.168.90.204:10001")
    zk.start()

    # start_path = "/udal_cluster"
    # zk = KazooClient(hosts="192.168.90.207:2181")
    # zk.start()

    nodes = zk.get_children(start_path) or []
    print_node_all_childs(zk, start_path)

    # # start_path = "/udal_cluster/"
    # data: Optional[Tuple] = zk.get(start_path)
    # print("data", data)
    zk.stop()
