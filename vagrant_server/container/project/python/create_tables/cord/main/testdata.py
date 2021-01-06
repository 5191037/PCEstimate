def testdata():
    testdata = {'cpu': [{'clock': '3.7GHz', 
                        'GEN': '4', 
                        'multi_thread': '○', 
                        'cache_2nd': '3', 
                        'cache_3rd': '32', 
                        'turbo_clock': '4.6GHz', 
                        'cores': '6', 
                        'thread': '12', 
                        'socket': 'Socket AM4', 
                        'TDP': '65W', 
                        'image_link': 'https://cdn.jisaku.com//images/3b91dd1304a37036.jpg/720.jpg', 
                        'name': 'AMD Ryzen 5 5600X BOX', 
                        'dospara': {'value': 39380, 'status': '在庫', 'link': 'https://www.dospara.co.jp/5shopping/detail_parts.php?ic=469252'}, 
                        'sofmap': {'value': 39380, 'status': '在庫', 'link': 'https://www.sofmap.com/product_detail/exec/?sku=21464382'}, 
                        'kakaku': {'value': 39380, 'status': '不明', 'link': 'https://kakaku.com/item/K0001299539/'}}], 
                
                'memory': [{'capacity': '8GB', 
                            'interface': 'DIMM', 
                            'piece': '2', 
                            'mem_stndrd': 'DDR3-1600', 
                            'image_link': 'https://cdn.jisaku.com//images/75006280dde77baa.jpg/720.jpg', 
                            'name': 'CFD W3U1600PS-8G [DDR3 PC3-12800 8GB 2枚組]', 
                            'kakaku': {'value': 5918, 'status': '不明', 'link': 'https://kakaku.com/item/K0000596705/'}}], 
                            
                'gpu': [{'cuda': '8704', 
                        'chip': 'GeForce RTX 3080', 
                        'bus_interface': 'PCI Express 4.0', 
                        'mem_bus': '320', 
                        'memory': 'GDDR6X 10GB', 
                        'image_link': 'https://cdn.jisaku.com/images/2077d41c93b5fbeee257d8959c16939c972ddc935c9903ee763e60bc8c6f2821.jpeg/tiny.webp', 
                        'name': 'MSI GeForce RTX 3080 GAMING X TRIO 10G [PCIExp 10GB]', 
                        'sofmap': {'value': 113300, 'status': '不明', 'link': 'https://www.sofmap.com/product_detail/exec/?sku=21275218'}, 
                        'kakaku': {'value': 113300, 'status': '不明', 'link': 'https://kakaku.com/item/K0001285835/'}}], 
                        
                'cpu-cooler': [{'type': 'サイドフロー型', 
                                'thickness': '83mm', 
                                'height': '154mm', 
                                'socket': 'LGA1150,LGA1151,Socket AM4,Socket AM3,LGA1366,Socket FM2,LGA2011-3,Socket AM3+,LGA2011,LGA1155,Socket FM2+,Socket AM2+,Socket FM1,LGA1156,LGA775,Socket AM2', 
                                'width': '130mm', 
                                'image_link': 'https://cdn.jisaku.com/images/955a8e0881ee44d76cb3e5909ee25c87ae28cb7f5b19bacf6ae649055d03e8c2.jpeg/tiny.webp', 
                                'name': 'サイズ 虎徹 MarkII SCKTT-2000', 
                                'dospara': {'value': 3828, 'status': '在庫', 'link': 'https://www.dospara.co.jp/5shopping/detail_parts.php?ic=446458'}, 
                                'sofmap': {'value': 3828, 'status': '在庫', 'link': 'https://www.sofmap.com/product_detail/exec/?sku=16623954'}, 
                                'kakaku': {'value': 3828, 'status': '不明', 'link': 'https://kakaku.com/item/K0000966603/'}, 
                                'amazon': {'value': 5840, 'status': '在庫', 'link': 'https://www.amazon.co.jp/dp/B072PWL5YF?tag=cjmarketing0a-22'}}], 
                                
                'motherboard': [{'audio': 'Realtek ALC S1200A', 
                                'chipset': 'AMD B550', 
                                'crossfire': '○', 
                                'formfactor': 'ATX', 
                                'max_memory': '128GB', 
                                'lan_speed': '10/100/1000/2500', 
                                'memory_slot': '4', 
                                'sata_slot': '6', 
                                'memory_type': 'DIMM DDR4', 
                                'Socket': 'SocketAM4', 
                                'image_link': 'https://cdn.jisaku.com/images/f40c3bb5c6a3270619295255f350df5e9e5d80e86e3e95f35aed5369a45540b0.jpeg/tiny.webp', 
                                'name': 'ASUS TUF GAMING B550-PLUS', 
                                'dospara': {'value': 15390, 'status': '在庫', 'link': 'https://www.dospara.co.jp/5shopping/detail_parts.php?ic=466996'}, 
                                'kakaku': {'value': 15390, 'status': ' 不明', 'link': 'https://kakaku.com/item/K0001259409/'}, 
                                'sofmap': {'value': 15400, 'status': '在庫', 'link': 'https://www.sofmap.com/product_detail/exec/?sku=20875773'}, 
                                'amazon': {'value': 18480, 'status': '在庫', 'link': 'https://www.amazon.co.jp/dp/B089XXHY6K?tag=cjmarketing0a-22'}}], 
                                
                'ssd': [{'capacity': '500GB', 
                        'interface': 'Serial ATA 6Gb/s', 
                        'speed-read': '560 MB/s', 
                        'speed-write': '510 MB/s', 
                        'image_link': 'https://cdn.jisaku.com/images/0a43e025f283f60a2022438f17b2b2d852a48c43f40b0f2bf016739bb33f682d.jpeg/tiny.webp', 
                        'name': 'Crucial MX500 CT500MX500SSD1/JP', 
                        'kakaku': {'value': 6080, 'status': '不明', 'link': 'https://kakaku.com/item/K0001028334/'}, 
                        'amazon': {'value': 6182, 'status': '在庫', 'link': 'https://www.amazon.co.jp/dp/B077PPN5NN?tag=cjmarketing0a-22'}, 
                        'dospara': {'value': 6880, 'status': '在庫', 'link': 'https://www.dospara.co.jp/5shopping/detail_parts.php?ic=456177'}, 
                        'sofmap': {'value': 8780, 'status': '在庫', 'link': 'https://www.sofmap.com/product_detail/exec/?sku=17542516'}}], 
                        
                'hdd': [{'size': '3.5インチ', 
                        'capacity': '6TB', 
                        'interface': 'SATA 3', 
                        'rpm': '5400', 
                        'thickness': '', 
                        'image_link': 'https://cdn.jisaku.com/images/60e351fb58360a99bfa054ff8a31b9d88276164481996d72d502bb9a024cae5e.jpeg/tiny.webp', 
                        'name': 'Western Digital WD60EZAZ-RT [6TB SATA600 5400]', 
                        'dospara': {'value': 10106, 'status': '在庫', 'link': 'https://www.dospara.co.jp/5shopping/detail_parts.php?ic=458341'}, 
                        'sofmap': {'value': 10106, 'status': '在庫', 'link': 'https://www.sofmap.com/product_detail/exec/?sku=19026158'}, 
                        'kakaku': {'value': 10106, 'status': '不明', 'link': 'https://kakaku.com/item/K0001133799/'}, 
                        'amazon': {'value': 12936, 'status': '在庫', 'link': 'https://www.amazon.co.jp/dp/B07MYKZGVX?tag=cjmarketing0a-22'}}], 
                        
                'power-supply': [{'80PLUS': 'Gold', 
                                'capacity': '850W', 
                                'plugin_available': '○', 
                                'standard': 'ATX/EPS', 
                                'image_link': 'https://cdn.jisaku.com/images/03b0b5211d2aae4608db077e81c74b811775eb57bd831336430a532f60e496e1.jpeg/tiny.webp', 
                                'name': 'Thermaltake Toughpower Grand RGB 850W Gold PS-TPG-0850FPCGJP-R [Black]', 
                                'dospara': {'value': 10978, 'status': '在庫', 'link': 'https://www.dospara.co.jp/5shopping/detail_parts.php?ic=445353'}, 
                                'kakaku': {'value': 10978, 'status': '不明', 'link': 'https://kakaku.com/item/K0000956406/'}, 
                                'amazon': {'value': 14417, 'status': '在庫', 'link': 'https://www.amazon.co.jp/dp/B01MXY5350?tag=cjmarketing0a-22'}, 
                                'sofmap': {'value': 14418, 'status': '在庫', 'link': 'https://www.sofmap.com/product_detail/exec/?sku=16452008'}}], 
                                
                'pc-case': [{'80PLUS': 'Gold', 
                            'capacity': '850W', 
                            'plugin_available': '○', 
                            'standard': 'ATX/EPS', 
                            'image_link': 'https://cdn.jisaku.com/images/03b0b5211d2aae4608db077e81c74b811775eb57bd831336430a532f60e496e1.jpeg/tiny.webp', 
                            'name': 'Thermaltake Toughpower Grand RGB 850W Gold PS-TPG-0850FPCGJP-R [Black]', 
                            'dospara': {'value': 10978, 'status': '在庫', 'link': 'https://www.dospara.co.jp/5shopping/detail_parts.php?ic=445353'}, 
                            'kakaku': {'value': 10978, 'status': '不明', 'link': 'https://kakaku.com/item/K0000956406/'}, 
                            'amazon': {'value': 14417, 'status': '在庫', 'link': 'https://www.amazon.co.jp/dp/B01MXY5350?tag=cjmarketing0a-22'}, 
                            'sofmap': {'value': 14418, 'status': '在 庫', 'link': 'https://www.sofmap.com/product_detail/exec/?sku=16452008'}}], 
                            
                'case-fan': [{'connector': '4pin', 
                            'size': '120mm', 
                            'led_writing': '○', 
                            'noise': '27dB', 
                            'max_rpm': '1800rpm', 
                            'PWM': '○', 
                            'image_link': 'https://cdn.jisaku.com/images/b5874681ca6e1f3454b2fcda3e4071bee59c8953fc5f440e7e75e631315c9887.jpeg/tiny.webp', 
                            'name': 'In Win Sirius Loop ASL120 ASL120FAN-3PK', 
                            'dospara': {'value': 2728, 'status': '在庫', 'link': 'https://www.dospara.co.jp/5shopping/detail_parts.php?ic=463308'}, 
                            'kakaku': {'value': 2728, 'status': '不明', 'link': 'https://kakaku.com/item/K0001176212/'}, 
                            'amazon': {'value': 3931, 'status': '在庫', 'link': 'https://www.amazon.co.jp/dp/B07TTSWCKV?tag=cjmarketing0a-22'}}]}
    return testdata