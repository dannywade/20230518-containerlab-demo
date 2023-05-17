# 20230518-containerlab-demo
Demo code for containerlab TTTT - May 2023

## Usage

### Installation

Install containerlab for your appropriate operating system. Check out the installation docs for more info: [containerlab installation docs](https://containerlab.dev/install/)

After installation, ensure containerlab is installed on your system by using the following command:
```
containerlab version
```

And you should see a similar output to the following (version may vary):
```

                           _                   _       _
                 _        (_)                 | |     | |
 ____ ___  ____ | |_  ____ _ ____   ____  ____| | ____| | _
/ ___) _ \|  _ \|  _)/ _  | |  _ \ / _  )/ ___) |/ _  | || \
( (__| |_|| | | | |_( ( | | | | | ( (/ /| |   | ( ( | | |_) )
\____)___/|_| |_|\___)_||_|_|_| |_|\____)_|   |_|\_||_|____/

    version: 0.41.0
     commit: acbc0e62
       date: 2023-05-11T17:35:13Z
     source: https://github.com/srl-labs/containerlab
 rel. notes: https://containerlab.dev/rn/0.41/
```

### Deploying a lab in containerlab

**Topology definition**: The containerlab topology is defined in `tttt.clab.yml`. Check out that file for more details about the nodes being deployed in the lab. If you have any questions about specific properties, here's a link to containerlab's node documentation: [node docs](https://containerlab.dev/manual/nodes/)

To deploy the lab, use the following command:
```
containerlab deploy -t tttt.clab.yml
```

If deployed successfully, you should see the following output:
```
+---+-------------+--------------+--------------+-------+---------+--------------------+--------------+
| # |    Name     | Container ID |    Image     | Kind  |  State  |    IPv4 Address    | IPv6 Address |
+---+-------------+--------------+--------------+-------+---------+--------------------+--------------+
| 1 | eos1        | 2ce89e553396 | ceos:4.28.4M | ceos  | running | 172.100.100.130/24 | N/A          |
| 2 | eos2        | 69d9c22c81ed | ceos:4.28.4M | ceos  | running | 172.100.100.131/24 | N/A          |
| 3 | netauto-box | 523fff6c7e18 | python:slim  | linux | running | 172.100.100.129/24 | N/A          |
+---+-------------+--------------+--------------+-------+---------+--------------------+--------------+
```

### Accessing the nodes

All nodes are accessible via `docker exec`, as each node is just a Docker container. Here's a quick example of how to access the shell of the `netauto-box` container:
```
docker exec -it netauto-box bash
```

For the Arista cEOS network devices, you can access via SSH using their hostnames (`eos1`, `eos2`). This is made possible by containerlab's automatic process of adding each node as host entries in `/etc/hosts`. Here's a snippet from the build logs that proves it:
```
INFO[0049] Adding containerlab host entries to /etc/hosts files
```

I just covered the basics to deploying the demo code. I highly recommend checking out the official docs to learn more: [containerlab docs](https://containerlab.dev/)

## Contribution

As most of this repository contains introductory demo code, there are definitely ways to improve the lab or even build more complex labs! Please feel free to make a pull request with whatever changes you think would help improve the lab!

## Feedback

If you have any questions or would like to provide further feedback, please feel free to message me or open an issue. Thanks!