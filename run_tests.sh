for testscript in test_*.py; do 
    echo "==> $testscript"
    python $testscript
done
