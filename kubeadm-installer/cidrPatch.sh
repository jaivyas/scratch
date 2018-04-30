for i in $(kubectl get nodes | awk '{print $1}' | grep -v NAME); do kubectl patch node $i -p '{"spec":{"podCIDR":"10.96.0.0/24"}}';done
