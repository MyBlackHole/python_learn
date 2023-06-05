import rtslib


def createTarget():
    fio = rtslib.FileIOStorageObject(
        "disk0", dev="/tmp/disk0.img", size=100 * 1024 * 1024
    )
    iscsiMod = rtslib.FabricModule("iscsi")
    tgt = rtslib.Target(iscsiMod, mode="create")
    tpg = rtslib.TPG(tgt, tag=None, mode="create")
    rtslib.LUN(tpg, lun=None, storage_object=fio)

    # 免密
    tpg.set_attribute("generate_node_acls", "1")
    tpg.set_attribute("cache_dynamic_acls", "1")
    tpg.set_attribute("authentication", "0")
    tpg.set_attribute("demo_mode_write_protect", "0")
    tpg.enable = True
    rtslib.NetworkPortal(tpg, "0.0.0.0", mode="create")
    return tgt.wwn


print(createTarget())
